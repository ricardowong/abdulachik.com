blog
    .controller('ContactController', ['$scope', '$http', function ($scope, $http) {
    // Send mail
    $scope.notification = {
      type: 'success',
      message: 'Select a subject from the list, complete the captcha and send me a message!'
    }

    $scope.message = {}
    $scope.postForm = {}
    $scope.message.subject = {
        choices : ["Contact", "Business" , "Other subject" ]
    }
    $scope.percentage = -1;
    $scope.send = function () {

        $scope.postForm = $scope.message;
        $scope.postForm.subject = $scope.postForm.subject.selected;
        console.log($scope.postForm);
        // CAPTCHA VALIDATION

        // AFTER SUCCESS SEND MESSAGE
        $http.post("/contact-me", $scope.postForm)
            .success(function(response){
                $scope.notification = {
                    show: true,
                    message : response.response,
                    type : "success"
                };
                $scope.message = {
                  subject : {
                    choices: ["Contact", "Business" , "Other subject"]
                  }
                };
            })
            .error(function(response){
                $scope.notification = {
                    show: true,
                    message : "Couldn't send the email!",
                    type : "warning"
                };

                $scope.message = {
                  subject : {
                    choices: ["Contact", "Business" , "Other subject"]
                  }
                };

            });
    }
}]);
