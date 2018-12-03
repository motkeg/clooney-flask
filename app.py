from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


from clooney_model.run import get_result
import os ,shutil

    

app = Flask(__name__)
dropzone = Dropzone(app)


app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB




@app.route('/', methods=['GET', 'POST'])
def index():
    # clean the "/upload folder"
    #if os.path.isdir('uploads/'):
    #    shutil.rmtree('uploads/')

    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            
            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )

            # append image urls
            file_urls.append(photos.url(filename))
            
        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request    
    return render_template('upload.html')

""" 
@app.route('/results')
def results():
    
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    
    return render_template('results.html', file_urls=file_urls) """

@app.route('/results')
def results():
    
    resultsrows = [['image name' , 'label']]
    

    for imgname in os.listdir(os.path.join("uploads")):
        score  = get_result(f"uploads/{imgname}")
        resultsrows.append([imgname , score])
    #print(resultsrows)    
        
    return render_template('results.html', scores=resultsrows)    

		
if __name__ == '__main__':
   app.run(debug = True)