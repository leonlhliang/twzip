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
        },
        clean: [
            "postal/*/*.json"
        ]
    });

    grunt.loadNpmTasks("grunt-contrib-jshint");
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.registerTask("default", ["jshint"]);

};
