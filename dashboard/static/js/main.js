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
  foodData.forEach((element)=>{
    let childNode = document.createElement('li');
    let textnode = document.createTextNode(element.product_name);
    childNode.appendChild(textnode);
    childNode.addEventListener('click', (e)=>{
      item = element;
      projector.innerHTML = element.product_name;
      projector.append(createDiv(element));
    });
    parent.appendChild(childNode);
  });
};

// creting projection div to display the content of the selected item
let createDiv = (item)=>{
  const SEARCH_LIST = {'sugars_100g':'Sugar/100g', 'fat_100g':'Fat/100g', 'cholesterol_100g':'Cholesterol/100g', 'carbohydrates_100g':'Carbohydrates/100g', 'fiber_100g':'Fiber/100g', 'proteins_100g':'Protein/100g', 'salt_100g':'Salt/100g', 'sodium_100g':'Sodium/100g'};
  let table = document.createElement('table');
  table.setAttribute('class', 'table table-striped table-hover');
  for(const [key, value] of Object.entries(item)){
    if (key in SEARCH_LIST) {
      let tr = document.createElement('tr');
      let td1 = document.createElement('td');
      let data = document.createTextNode(SEARCH_LIST[key]);
      td1.appendChild(data);

      let td2 = document.createElement('td');
      data = document.createTextNode(value);
      td2.appendChild(data);

      tr.appendChild(td1);
      tr.appendChild(td2);
      table.appendChild(tr);
    }
  }
  return table;
};

// cart contains the objects of selected food
let cart = []

// adding item to cart and displaying on cartview
document.querySelector(".projection button").addEventListener('click', ()=>{
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
document.querySelector('#record-nutrition').addEventListener('click',()=>{
  inputField = document.createElement('input');
  inputField.setAttribute("name", "foodItems")
  inputField.setAttribute("type","text");
  inputField.hidden = true;
  let val = "";
  for (let counter=0; counter<cart.length; counter++){
    val = val + cart[counter].id + " ";
  }
  val = val.substring(0, val.length-1);
  inputField.setAttribute('value', val);
  form = document.querySelector('#nutritionIntakeForm');
  form.appendChild(inputField);
  if (document.querySelector('#nutritionIntakeForm input[type=date]').value === ''){
    let error = document.createElement('p');
    error.append(document.createTextNode('**please select date first.'));
    error.setAttribute('color','#ff0000');
    error.setAttribute('id','error-tag');
    document.querySelector('#nutritionIntakeForm').appendChild(error);
  }
  else {
    document.querySelector('#nutritionIntakeForm').submit();
  }
})
