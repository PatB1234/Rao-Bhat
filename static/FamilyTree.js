var fTree = [{ id: 1, pids: [2], name: "King George VI", img: "https://cdn.balkan.app/shared/f1.png", gender: 'male' }]

function getTree() {

    axios.get('/get_tree')
        .then(function (response) {

            for (let i = 0; i < response.data.length; i++) {

                data = response.data[i]
                fTree.append = ({ name: data[0], id: data[5], place: [3], marital_status: [4], born: [1], died: [2] });
            }
        })

        .catch(function (error) {

            console.log(error);
        })
}
getTree()
var chart = new FamilyTree(document.getElementById("tree"), {
    mouseScrool: FamilyTree.none,
    siblingSeparation: 120,
    template: 'john',
    nodeBinding: {
        field_0: "name"
    }
});
chart.load(fTree);