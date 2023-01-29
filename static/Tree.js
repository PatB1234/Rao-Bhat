fTree = []

var chart = new FamilyTree(document.getElementById("tree"), {
    mouseScrool: FamilyTree.none,
    siblingSeparation: 10,
    nodeBinding: {
        field_0: "Name"
    }
});
function treeStuff() {
    axios.get('/get_tree')
        .then(function (response) {
            for (let i = 0; i < response.data.length; i++) {

                datar = response.data[i]
                var uID;

                if (typeof (datar[5]) == "number") {

                    uID = datar[5];
                } else {

                    uID = datar[5][0];
                }

                if (datar[4] == false) {
                    if (datar[2] != null) {

                        fTree.push({ id: uID, mid: datar[6], pid: datar[7], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
                    } else {

                        fTree.push({ id: uID, mid: datar[6], pid: datar[7], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
                    }

                } else {

                    if (datar[2] != null) {

                        fTree.push({ id: uID, pids: [datar[6]], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
                    } else {

                        fTree.push({ id: uID, mid: datar[5][2], fid: datar[5][1], pids: [datar[5][3]], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
                    }

                }
            }
            console.log(fTree);
            chart.load(fTree);
        })

        .catch(function (error) {

            console.log(error);
        })
}

treeStuff()