abdulBlog
	.controller('DashboardController', ['$scope', '$http', '$filter', function($scope, $http, $filter){
		$scope.postForm = {};
		$scope.createPost = false;
		$scope.posts = {};
		$scope.postForm.tags = [];
		$http.get('/post/all').success(function(response){
			$scope.posts = response;
		});

		$http.get('/tag/all').success(function(response){
			$scope.tags = response;
		});

		$scope.$watch('posts', function(data){
			$scope.posts = data;
		});

		$scope.$watch('postForm.tags', function(data){
			console.log(data);
			try{
				console.log("postForm.tags try")
				$scope.tags.map(function(tag){
					console.log(tag);
					var selected;
					$scope.postForm.tags.map(function(pTag){
						tag.selected = tag.selected ? true : pTag.id == tag.id;
					});
					return tag;
				});
			} catch(e){console.log(e)}
		});
		$scope.newPost = function(publish){
			$scope.postForm.published = publish;
			$http.post('/post/new', $scope.postForm).success(function(response){
				$scope.createPost = !$scope.createPost;
				$scope.posts.push(response);
				$scope.postForm = {};
				if ($scope.postForm.tags){
					console.log("hay tags!", $scope.postForm.tags);
					$http.post('/tagpost/' + response.id, { "tags" : $scope.postForm.tags }).success(function(response){
						$scope.postForm.tags = [];
					});
				};
			});
		};

		$scope.updatePost = function(post){
			var url = '/post/' + post.id
			$http.put(url, post).success(function(success){
				$scope.postForm = {};
				if ($scope.postForm.tags){
					console.log("updateTags", $scope.postForm.tags);
					$http.put('/tagpost/' + response.id, { "tags" : $scope.postForm.tags }).success(function(response){
						$scope.postForm.tags = [];
					});
				};
			});
		};

		$scope.deletePost = function(post){
			var url = '/post/' + post.id;
			var index = $scope.posts.indexOf(post);
			$scope.posts.splice(index, 1);
			$http.delete(url, post.id);
		};

		$scope.addTag = function(tag){
			$http.post('/tag/new', { "title" : tag })
			.success(function(response){
				$scope.tagTitle = "";
				$scope.tags.push(response);
			});
		};

		$scope.tagPost = function(tag){
			console.log("tag", tag);
			tag.selected = true;
			$scope.postForm.tags.push(tag);
		};

		$scope.untagPost = function(tag){
			console.log("untag", tag);
			tag.selected = false;
			var index = $scope.postForm.tags.indexOf(tag);
			console.log(index);
			$scope.postForm.tags.splice(index, 1);
		};
	}]);	