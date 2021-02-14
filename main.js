 let {PythonShell} = require('python-shell');

PythonShell.run('run.py',  function  (err, results)  {
 if  (err)  console.log(err);

 console.log('results', results);
});


const {app, BrowserWindow} = require('electron')



 function createWindow () {
     const window = new BrowserWindow({
         width : 900,
         height : 600,

         webPreferences: {
             contextIsolation: true
         }
     })
    window.loadFile("" +
        "index.html")
    }






   app.on('ready', createWindow)


app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })


 const { ipcMain } = require('electron')

ipcMain.on(`asynchronous`, (event, arg) => {
  console.log(`asynchronous`,arg)
  event.sender.send("async",'IPC MAIN ASYNC')
})

ipcMain.on('synchronous', (event, arg) => {
  console.log('synchronous',arg) // prints "ping"
  event.returnValue = 'pong'
})




