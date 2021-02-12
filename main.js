const {app, BrowserWindow} = require('electron')


 function createWindow () {
     const window = new BrowserWindow({
         width : 900,
         height : 600,

         webPreferences: {
             contextIsolation: true
         }
     })
    window.loadFile('index.html')




  }





   app.on('ready', createWindow)






app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })

let {PythonShell} = require('python-shell');





PythonShell.run('run.py',  function  (err, results)  {
 if  (err)  console.log(err);
});




