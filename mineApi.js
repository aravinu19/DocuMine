var extract_text = require('pdf-text-extract');
var fs = require('fs');
var { exec } = require('child_process');

var mineApi = (app) => {
    
    app.post("/mine", (req, res) => {

        if(Object.keys(req.files).length == 0){
            console.log("Improper Request without a file uploaded");
            return res.status(400).send("No file to process");
        }

        let the_file_mine = req.files.zipFile;

        the_file_mine.mv('./main_program_dir/uploaded_file.txt', (err) => {
            if (err) {
                console.log(err);
                return res.status(500).send(err);
            }
        });

        exec(`cd main_program_dir && python tfidf_nlp.py -t uploaded_file.txt`, (err, stdout, stderr) => {
            if (err) {
                console.log(err);
                return;
            }

            console.log(`STDERR ${stderr}`);
            console.log(`STDOUT ${stdout}`);



        })

        console.log('File Processed Successfully !');
        res.send('File Received and Processed !');

    });

};

module.exports = mineApi;