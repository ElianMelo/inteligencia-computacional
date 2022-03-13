row = 5
col = 3

values = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1];
position = {};
position.val = 1;
for (let r = 0; r < row; r++) {
    let rowElement = $("<div class='row'>")
    for(let c = 0; c < col; c++) {
        let newPosition = position.val;
        let colElement = $("<div class='col box boxBlue'>")
            .attr('id', newPosition)
            .click(function(){
                calcItem(newPosition);
            });
        rowElement.append(colElement)
        position.val += 1;
    }
    $("#numpad").append(rowElement)
}

var calculatedWeight = calcAllWeight();

function calcItem(position) {
    let id = "#" + position;
    let e = $(id);

    if(e.hasClass("boxBlue")) {
        e.removeClass("boxBlue")
        .addClass("boxRed");
        values[position-1] = 1;
    } else {
        e.removeClass("boxRed")
        .addClass("boxBlue");
        values[position-1] = -1;
    }
}

function calcPerceptron() {
    newValues = [...values]
    newValues.unshift(1);
    let neuron1 = testWeight(calculatedWeight[0], newValues);
    let neuron2 = testWeight(calculatedWeight[1], newValues);
    if (neuron1 == 1 && neuron2 == 1) {
        alert("0");
    } else if (neuron1 == 1 && neuron2 == -1) {
        alert("1");
    } else if (neuron1 == -1 && neuron2 == 1) {
        alert("2");
    } else if (neuron1 == -1 && neuron2 == -1) {
        alert("3");
    }
}