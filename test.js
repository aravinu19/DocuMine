var fs = require('fs');

var daataa = fs.readdirSync('main_program_dir');

daataa.forEach(element => {
    if (element.toString().includes('.p')) {
        console.log(element.toString());
    }
});