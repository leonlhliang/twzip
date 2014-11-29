module.exports = function () {
    this.Given(/^The server is running$/, function (next) {
        next.pending();
    });

    this.When(/^Send request to "([^"]*)"$/, function (url, next) {
        next.pending();
    });

    this.Then(/^Got response status code "([^"]*)"$/, function (status, next) {
        next.pending();
    });
};
