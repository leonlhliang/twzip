module.exports = function (grunt) {
    grunt.initConfig({
        jshint: {
            options: {
                globals: {
                    node: true
                }
            },
            files: [
                "features/step_definitions/**/*.js",
                "server.js"
            ]
        }
    });
    grunt.loadNpmTasks("grunt-contrib-jshint");
    grunt.registerTask("default", ["jshint"]);
};
