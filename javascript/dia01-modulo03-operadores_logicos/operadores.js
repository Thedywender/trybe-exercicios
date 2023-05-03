/* let currentHour = 1;
let message;

if (currentHour < 0 || currentHour > 24) {
    message = "Adicione uma hora válida"
} else if(currentHour >= 22) {
    message = "Não deveriamos comer nada, é hora de dormir"
} else if (currentHour >= 18 && currentHour < 22) {
    message = "Rango da noite, vamos jantar :D"
} else if(currentHour >= 14 && currentHour < 18) {
    message = "Vamos fazer um bolo pro café da tarde?"
} else if(currentHour >= 11 && currentHour < 14) {
    message = "Hora do almoço !!!"
} else if(currentHour > 4 && currentHour < 11) {
    message = "Hmmm, cheiro de café recém-passado"
} else {
    message = "Não deveria estar acordado!!!"
}

console.log(message); */

let weekDay = ["segunda-feira", "terça-feira", 'quarta-feira', 'quinta-feira', 'sextas-feira'];
let weekEnds = ['sabado', 'domingo'];
let day = weekDay[2];
let message;

if(day == weekDay[2]) {
    message = "Oba, mais um dia de aprendizado na Trybe >:D"
} else {
    message = "FINALMENTE, descanso merecido! UwU!"
}

console.log(`${message} hoje é ${day}!`);