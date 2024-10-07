const PostList = {
    data() {
        return {
            posts: [],
            interval: null,
        }
    },
    mounted(){
        axios.get('/postJson')
        .then(function(response){
            myapp.posts=response.data.posts;
            console.log(response);
        })
        .catch(function (error){
            console.log(error);
        })
        this.interval = setInterval(()=> {
            axios.get('/postJson')
            .then(function(response){
                myapp.posts=response.data.posts;
                console.log(response);
            })
            .catch(function (error){
                console.log(error);
            })
        },10000)
    },
    umounted(){
        clearInterval(this.interval);
    }
}
myapp = Vue.createApp(PostList).mount('#post-list')