const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

// Function to create directory if it doesn't exist
const createDirectoryIfNotExists = (directory) => {
    if (!fs.existsSync(directory)) {
        fs.mkdirSync(directory, { recursive: true });
    }
};

// Function to download a file from a URL
const downloadFile = (url, filePath) => {
    const protocol = url.startsWith('https') ? https : http;
    return new Promise((resolve, reject) => {
        protocol.get(url, (response) => {
            const fileStream = fs.createWriteStream(filePath);
            response.pipe(fileStream);
            fileStream.on('finish', () => {
                fileStream.close();
                resolve();
            });
            fileStream.on('error', (err) => {
                fs.unlink(filePath, () => reject(err));
            });
        }).on('error', (err) => {
            fs.unlink(filePath, () => reject(err));
        });
    });
};

// Main function to read JSON file and initiate downloads
const main = async () => {
    try {
        const folderPath = './arquivos/2015';
        createDirectoryIfNotExists(folderPath);

        const jsonFilePath = './arquivos/dissertação-2015.json';
        const jsonData = fs.readFileSync(jsonFilePath, 'utf8');
        const urlList = JSON.parse(jsonData);

        for (const url of urlList) {
            const fileName = path.basename(url);
            const filePath = path.join(folderPath, fileName);
            await downloadFile(url, filePath);
            console.log(`File '${fileName}' downloaded successfully.`);
        }

        console.log('All files downloaded successfully.');
    } catch (error) {
        console.error(`An error occurred: ${error.message}`);
    }
};

// Run the main function
main();
