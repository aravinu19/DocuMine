var mineApi = (app) => {
    
    app.post("/mine", (req, res) => {

        if(Object.keys(req.files).length == 0){
            console.log("Improper Request without a file uploaded");
            return res.status(400).send("No file to process");
        }

        let the_file_mine = req.files.zipFile;

        the_file_mine.mv('/main_program_dir/zipFile.zip', (err) => {
            if (err) {
                return res.status(500).send(err);
            }
        });

        res.send('File Received and Processed !');

    });

};