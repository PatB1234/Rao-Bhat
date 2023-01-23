fTree = []

var chart = new FamilyTree(document.getElementById("tree"), {
    mouseScrool: FamilyTree.none,
    siblingSeparation: 10,
    nodeBinding: {
        field_0: "Name"
    }
});

axios.get('/get_tree')
    .then(function (response) {

        for (let i = 0; i < response.data.length; i++) {

            datar = response.data[i]
            if (datar[2] != null) {

                fTree.push({ id: datar[5], pids: [datar[6], datar[7]], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
            } else {

                fTree.push({ id: datar[5], pids: [datar[6], datar[7]], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
            }
        }
        console.log(fTree)
        chart.load(fTree);
    })

    .catch(function (error) {

        console.log(error);
    })

