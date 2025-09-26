public class Doubles {

    static class Node {
        int data;
        Node next;
        Node prev;

        Node(int data) {
            this.data = data;
            this.next = null;
            this.prev = null;
        }

    }

    public static void main(String[] args) {
        Node first = new Node(3);
        Node second = new Node(4);
        Node third = new Node(7);
        Node fourth = new Node(9);

        first.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = first;

        first.prev = fourth;
        second.prev = first;
        third.prev = second;
        fourth.prev = third;

        Node current = first;
        while (current != null){
            System.out.println(current.data + " ->");
            current = current.prev;
        }
    }
}
