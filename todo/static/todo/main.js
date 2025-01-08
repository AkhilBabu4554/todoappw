
function emptycheck(event){
    form=document.getElementById('formid')
    task=document.getElementById('formtask').value.trim();
    if(task===""){
    event.preventDefault();
    alert("the task field cannot be empty")
}
}   
            
// function Doneornot(){
//     task=document.getElementById('task')
//     check=document.getElementById('check')
//     Status = check.textContent.trim();
//     if(Status==="Not Done"){
//         task.style.textDecoration = 'line-through';

//     }else{
//         task.style.textDecoration = 'none';
//     }

// }


