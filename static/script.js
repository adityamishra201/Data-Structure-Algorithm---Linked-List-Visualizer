function updateLinkedListView(list) {
    const listContainer = document.getElementById('linked-list');
    listContainer.innerHTML = ''; // Clear existing list
    
    list.forEach((node, index) => {
        const nodeDiv = document.createElement('div');
        nodeDiv.className = 'node';
        nodeDiv.textContent = node;
        listContainer.appendChild(nodeDiv);

        if (index < list.length - 1) {
            const arrowDiv = document.createElement('div');
            arrowDiv.className = 'arrow';
            listContainer.appendChild(arrowDiv);
        }
    });
}

function insertAtPosition() {
    const data = document.getElementById('nodeData').value;
    const index = parseInt(document.getElementById('nodeIndex').value);
    fetch('/linked-list', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: data, index: index }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            updateLinkedListView(data);
        }
    });
}

function deleteNode() {
    const data = document.getElementById('nodeData').value;
    fetch('/linked-list', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: data }),
    })
    .then(response => response.json())
    .then(data => updateLinkedListView(data));
}
