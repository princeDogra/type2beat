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
  let searchItem  = document.querySelector('#searchItem').value;
  const ENDPOINT = "/api/data/food/?search="+searchItem;
  $.ajax({
    method: "GET",
    url: ENDPOINT,
    success: function(data){
      foodData = data
      displayData()
    },
    error: function(error_data){
      console.log(error_data)
    }
  })
})
let displayData = () => {
  let parent = document.querySelector('#food-item-holder');
  let projector=document.querySelector('#projector');
  let counter = 0;
  let dict  =  new Object();
  foodData.forEach((element)=>{
    let childNode = document.createElement('li');
    let textnode = document.createTextNode(element.product_name);
    childNode.appendChild(textnode);
    childNode.id = counter;
    childNode.addEventListener('click', (e)=>{
      projector.innerHTML = element.product_name;
    });
    parent.appendChild(childNode);
    dict[''+counter]=element.id;
    counter+=1;
  });
  console.log(dict);
}
