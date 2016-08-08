app.controller('BlogIndexCtrl', function($scope, $rootScope){
   console.log("BlogIndex Ctrl");
});
app.controller('NewPostCtrl', function($scope, $rootScope, $http){
  $rootScope.dashboard.title = "New post";
  $rootScope.dashboard.subtitle = "create some awesome content right here";
  $scope.formData = {
    tags: []
  };
  $scope.preview = false;
  $scope.post = function(){
    $scope.formData.published = true;
    console.log($scope.formData);
    $http.post('/api/post/new', $scope.formData, function(response){
      $scope.formData = {};
    });
  }
  $scope.draft = function(){
    $scope.formData.published = false;
    $http.post('/api/post/new', $scope.formData, function(response){
      $scope.formData = {};
    });
  }

  $scope.cancel = function(){
    $scope.formData = {};
  }
  $scope.preview = function(){
    $scope.preview != $scope.preview;
  }
});

app.controller('TimelineCtrl', function($scope, $rootScope, $resource){
  $rootScope.dashboard.title = "Timeline";
  $rootScope.dashboard.subtitle = "quick access to your most recent posts"
  $resource('/api/post/all').get(function(value){
    $scope.posts = value.posts;
  });
});
