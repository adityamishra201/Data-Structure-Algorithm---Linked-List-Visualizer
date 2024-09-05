from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, index, data):
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        position = 1
        while current and position < index - 1:
            current = current.next
            position += 1
        if not current:
            return "Index out of bounds"
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def get_list(self):
        node = self.head
        result = []
        while node:
            result.append(node.data)
            node = node.next
        return result

linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/linked-list', methods=['POST', 'DELETE'])
def linked_list_operations():
    if request.method == 'POST':
        data = request.json.get('data')
        index = request.json.get('index')
        if index is not None:
            result = linked_list.insert_at_position(index, data)
            if result == "Index out of bounds":
                return jsonify({"error": "Index out of bounds"}), 400
    elif request.method == 'DELETE':
        data = request.json.get('data')
        linked_list.delete_node(data)

    return jsonify(linked_list.get_list())

if __name__ == '__main__':
    app.run(debug=True)
