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

let weekDay = ["Segunda-feira", "Terça-feira", 'Quarta-feira', 'Quinta-feira', 'Sexta-feira'];
let weekEnds = ['sabado', 'Domingo'];
let day = weekEnds[1];
let message;

if(day == weekDay[0] || day == weekDay[1] || day == weekDay[2] || day == weekDay[3] || day == weekDay[4] ) {
    message = "Oba, mais um dia de aprendizado na Trybe >:D"
} else if(day == weekEnds[0] || weekEnds[1]) {
    message = "FINALMENTE, descanso merecido! UwU!"
};

console.log(`${message} hoje é ${day}!`);