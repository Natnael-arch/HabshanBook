let addToCartBtns = document.getElementsByClassName('update-cart');


for(let i=0; i < addToCartBtns.length; i++){
    addToCartBtns[i].addEventListener('click', function(){
        let bookId = this.dataset.product;
        let action = this.dataset.action;
        console.log('bookId:',bookId);
        if(user === 'AnonymousUser'){
            console.log('user is not authenticated');
        }
        else {
            updateCart(bookId, action);
        }
    })}
    
    

function updateCart(bookId,action){
     console.log('user is logged in');
        let url = '/add_cart/'
		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'bookId':bookId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    console.log(data);
		});
}

    