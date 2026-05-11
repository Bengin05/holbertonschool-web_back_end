class AppController {
    static getHomepage(req, res) {
        res.status(200).send('Hello Holberton SChool!');
    }
}

export default AppController;
