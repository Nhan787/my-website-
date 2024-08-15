// app.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/process_login', (req, res) => {
    const email = req.body.email;
    const password = req.body.password;

    // Xử lý hoặc kiểm tra dữ liệu ở đây
    console.log(`Email: ${email}`);
    console.log(`Password: ${password}`);

    // Trả về phản hồi cho người dùng
    res.send(`Email: ${email}<br>Password: ${password}`);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
