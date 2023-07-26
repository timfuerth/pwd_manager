document.body.style.border = "5px solid red";

let inputs = document.getElementsByTagName("input")

Array.from(inputs).forEach(element => {
    
    switch (element.type.toLowerCase()) {
        case "password":
            element.value = "123"
            break;
        case "email":
            element.value = "abc@gmail.com"

        default:
            break;
    }

});


let ptags = document.getElementsByTagName("p")

for(let i = 0; i < ptags.length; i++){
    ptags[i].style.border = "5px solid red";
}
