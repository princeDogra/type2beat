const menuBtn = document.querySelector('.menu-btn');
const wrapper = document.querySelector('#wrapper');
let menuOpen = false;

menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        wrapper.classList.add('toggled');
        menuOpen = true;
    }
    else{
        menuBtn.classList.remove('open');
        wrapper.classList.remove('toggled');
        menuOpen = false;
    }
})

// =============================================================================
// loading food data from the database
// =============================================================================

let foodData = []

document.querySelector('#search-food-item').addEventListener('click', (e)=> {
  let searchItem  = document.querySelector('#searchItem');
  if (searchItem.value.length == 0) {
    searchItem.style.border = "3px solid rgba(222,100,0,0.7)";
    document.querySelector('#food-item-holder').innerHTML = "";
    document.querySelector('#projector').innerHTML = "";
  }
  else {
    searchItem.style.border = "3px solid #69BDBB";
    const ENDPOINT = "/api/data/food/?search="+searchItem.value;
    // make an ajax call to the rest-api
    $.ajax({
      method: "GET",
      url: ENDPOINT,
      success: function(data){
        if (data.length == 0) {
          document.querySelector('#food-item-holder').innerHTML = "No item found";
          document.querySelector('#projector').innerHTML = "";
        }
        else{
          foodData = data
          displayData()
        }
      },
      error: function(error_data){
        console.log(error_data)
      }
    })
  }
})

let item = null;

let displayData = () => {
  let parent = document.querySelector('#food-item-holder');
  parent.innerHTML = "";
  let projector=document.querySelector('#projector');
  projector.innerHTML = "";
  let counter = 0;
  let dict  =  new Object();
  foodData.forEach((element)=>{
    let childNode = document.createElement('li');
    let textnode = document.createTextNode(element.product_name);
    childNode.appendChild(textnode);
    childNode.id = counter;
    childNode.addEventListener('click', (e)=>{
      item = element;
      projector.innerHTML = element.product_name;
      projector.append(createDiv(element));
    });
    parent.appendChild(childNode);
    dict[''+counter]=element.id;
    counter+=1;
  });
};

// creting projection div to display the content of the selected item
let createDiv = (item)=>{
  const KEYS = Object.keys(item);
  const VALUES = Object.values(item);
  let table = document.createElement('table');
  table.classList.add('table');
  for(const [key, value] of Object.entries(item)){
    let tr = document.createElement('tr');
    let td1 = document.createElement('td');
    let data = document.createTextNode(key);
    td1.appendChild(data);

    let td2 = document.createElement('td');
    data = document.createTextNode(value);
    td2.appendChild(data);

    tr.appendChild(td1);
    tr.appendChild(td2);
    table.appendChild(tr);
  }
  return table;
};

// cart contains the objects of selected food
let cart = []

// adding item to cart and displaying on cartview
document.querySelector(".projection form button").addEventListener('click', ()=>{
  cart.push(item);
  if (cart.length > 0) {
    document.querySelector('#record-nutrition').disabled = false;
  }
  document.querySelector('#cart-view ul').innerHTML = "";
  cart.forEach(updateCart);
})


let updateCart = (element, index, array)=>{
  listItem = document.createElement('li');
  delButton = document.createElement('button');
  delButton.innerHTML = "Delete";
  delButton.classList.add('t2b-btn-delete');
  listItem.appendChild(document.createTextNode(element.product_name));
  listItem.appendChild(delButton);
  document.querySelector('#cart-view ul').appendChild(listItem);
  delButton.addEventListener('click', (e)=> {
    // find the index of the current node in the parent list
    indexOfItemToDelete = Array.from(e.currentTarget.parentNode.parentNode.children).indexOf(e.currentTarget.parentNode);
    e.currentTarget.parentNode.remove();
    cart.splice(indexOfItemToDelete, 1);
    if(cart.length == 0){
      document.querySelector('#record-nutrition').disabled = true;
    }
  });
}

// record button functionality onclick
document.querySelector('#record-nutrition').addEventListener('click', (e)=> {
  if (e.currentTarget.disabled == true){
    console.log('i cannot do anything');
  }
  else {
    e.currentTarget.submit();
  }
});
