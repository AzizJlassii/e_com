let productLabel = document.querySelector('.label').innerText;
let imgElement = document.querySelector('.imger').getAttribute('src');
let productPrice = document.querySelector('.price').innerText;



function AddToCar(){
    let products = JSON.parse(localStorage.getItem('products')) || [];
    products.push({label: productLabel, price: parseFloat(productPrice.substring(1)), imgsrc: imgElement   });
    localStorage.setItem('products', JSON.stringify(products));
}


let products = JSON.parse(localStorage.getItem('products')) || [];
let cartList = document.querySelector('.cart-list');

products.forEach(product => {
  let productWidget = document.createElement('div');
  productWidget.className = 'product-widget';
  productWidget.innerHTML = `
    <div class="product-img">
    <img src="${product.imgsrc}" alt="">

    </div>
    <div class="product-body">
      <h3 class="product-name"><a href="#">${product.label}</a></h3>
      <h4 class="product-price"><span class="qty">1x</span>$${product.price}</h4>
    </div>
    <button class="delete"><i class="fa fa-close"></i></button>
  `;
  cartList.appendChild(productWidget);
});

let total = 0;
products.forEach(product => {
  total += parseFloat(product.price);
});

let cartSummary = document.querySelector('.cart-summary');
cartSummary.innerHTML = `<small>${products.length} Item(s) selected</small><h5>SUBTOTAL: $${total.toFixed(2)}</h5>`;
