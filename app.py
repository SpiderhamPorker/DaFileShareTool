import web
import os
import shutil
urls = (
    '/', 'index'
)

class index:
    def GET(self):
        allfilesandfolders=os.listdir('static/')
        folder = './static/'
        sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
        render=web.template.render('templates/')
        print(sub_folders)
        for elements in sub_folders:
            filename=folder+elements+'zipped.zip'
            if os.path.isfile(filename):
                os.remove(filename)
            shutil.make_archive(
                elements+"zipped",
                'zip',
                root_dir=folder+elements,
                base_dir='.'
            )
            shutil.move(elements+'zipped.zip', './static')
        allfilesandfolders=os.listdir('static/')
        return render.template1(allfilesandfolders)       
if __name__ == "__main__":
    app=web.application(urls, globals())
    app.run()