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

// document.getElementById(".form").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent default form submission
//     var formData = {
//     "deal-satisfaction": document.getElementById(".dealSatisfaction").value,
//     "property_type": document.getElementById(".property").value,
//     "area": document.getElementById(".area").value,
//     "sale_month": document.getElementById(".saleMonth").value,
//     "sale_weekday": document.getElementById(".saleWeekday").value,
//     "birth_month": document.getElementById(".birthMonth").value,
//     "birth_year": document.getElementById(".birthYear").value,
//     "birth_weekday": document.getElementById(".birthWeekday").value,
//     "age": document.getElementById(".age").value
// };
// fetch("/api/predict1", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify(formData)
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//         // Process the response data here
//     })
//     .catch(error => {
//         console.error("Error:", error);
//     });
// });
// var test = document.querySelector(".form")
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
//     }}
// )
//     // If all inputs are filled, you can show the result
  
//     result.style.display = "block";
  
//   });