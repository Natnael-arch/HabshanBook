


let updateToCartBtns = document.getElementsByClassName('update-cart');
let addToCartBtns = document.getElementsByClassName('add-cart');

for(let i=0; i < addToCartBtns.length; i++){
    addToCartBtns[i].addEventListener('click', function(){
        let bookId = this.dataset.product;
        let action = this.dataset.action;
        console.log('bookId:', bookId);
        if(user === 'AnonymousUser'){
            console.log('user is not authenticated');
        }
        else {
            addCart(bookId, action);
        }
    })}
    
    

function addCart(bookId,action){
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

    
for(let i=0; i < updateToCartBtns.length; i++){
    updateToCartBtns[i].addEventListener('click', function(){
        let bookId = this.dataset.product;
        let action = this.dataset.action;
        console.log('bookId:', bookId);
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
		    location.reload();
		});
}
pbt = document.getElementById("purchase_button");
pbt.addEventListener("click", function(){
cart_table = document.getElementsByTagName("td");
cart_table.innerHTML = "";
}, false)