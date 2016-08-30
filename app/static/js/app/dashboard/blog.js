app.controller('BlogIndexCtrl', function($scope, $rootScope){
   console.log("BlogIndex Ctrl");
});
app.controller('NewPostCtrl', function($scope, $rootScope, $http){
  $rootScope.dashboard.title = "New post";
  $rootScope.dashboard.subtitle = "create some awesome content right here";
  $scope.formData = {
    tags: []
  };
  $scope.wysiwygOptions = {
    height:300,
    airmode:true,
    toolbar: [
      ['edit',['undo','redo']],
      ['headline', ['style']],
      ['style', ['bold', 'italic', 'underline', 'superscript', 'subscript', 'strikethrough', 'clear']],
      ['fontface', ['fontname']],
      ['textsize', ['fontsize']],
      ['fontclr', ['color']],
      ['alignment', ['ul', 'ol', 'paragraph', 'lineheight']],
      ['height', ['height']],
      ['table', ['table']],
      ['insert', ['link','picture','video','hr']],
      ['view', ['fullscreen', 'codeview']],
      ['help', ['help']]
    ]
  }
  $scope.isPreview = false;

  console.log($.summernote, $rootScope);
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
    $scope.isPreview = !$scope.isPreview;
  }
});

app.controller('TimelineCtrl', function($scope, $rootScope, $resource){
  $rootScope.dashboard.title = "Timeline";
  $rootScope.dashboard.subtitle = "quick access to your most recent posts"
  $resource('/api/post/all').get(function(value){
    $scope.posts = value.posts;
  });
});
