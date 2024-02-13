function handleClick() {
    // Get the first element with the class "menu-2"
    var element = document.getElementsByClassName("menu-2")[0];

    // Set the display style for the element
    if (element) {
        element.style.display = "block";
    }
}
function handle2Click(){
    var element = document.getElementsByClassName("menu-2")[0];
    if (element) {
        element.style.display = "none";
    }   
}

// var btn = document.querySelector("form")
// btn.addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent the default form submission
  
//     // Get form values
//     const deal_satisfaction = document.getElementById("1").value;
//     const property_type = document.getElementById("2").value;
//     const area = document.getElementById("3").value;
//     const sale_month = document.getElementById("4").value;
//     const sale_weekday = document.getElementById("5").value;
//     const birth_month = document.getElementById("6").value;
//     const birth_year = document.getElementById("7").value;
//     const birth_weekday = document.getElementById("8").value;
//     const age = document.getElementById("9").value;
  
//     // Create data object
//     const formData = {
//       "deal_satisfaction": parseInt(deal_satisfaction),
//       "property_type": parseInt(property_type),
//       "area": parseFloat(area),
//       "sale_month": parseInt(sale_month),
//       "sale_weekday": parseInt(sale_weekday),
//       "birth_month": parseInt(birth_month),
//       "birth_year": parseInt(birth_year),
//       "birth_weekday": parseInt(birth_weekday),
//       "age": parseInt(age)
//     };
  
//     // Make the POST request
//     fetch('http://127.0.0.1:5000/api/predict1', {
//       method: "POST",
//       mode: 'no-cors',
//       headers: {
//         'Access-Control-Allow_Origin': '*',
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(formData),
//     })
//       .then(response => response.json())
//       .then(data => {
//         console.log(data["prediction"])
//       })
//   });

// var test = document.querySelector("form")
// var result = document.querySelector(".result")
// test.addEventListener('submit', function (event) {
//     event.preventDefault();
//     for (var i = 1; i <= 9; i++) {
//       var inputField = document.getElementById(String(i));
  
//       if (inputField.value.trim() === '') {
//         alert('Please fill in all inputs');
//         // Prevent form submission
//         // Stop further validation if any input is empty
//       }
//     }
  
//     // If all inputs are filled, you can show the result
  
//     result.style.display = "block";
  
//   });