#include<iostream>
using namespace std;
class Node{
public:
    int data;
    Node* next;

    Node(int d){
        this->data = d;
        this->next = NULL;
    }
};

void insertAtHead(Node* &head, Node* &tail, int d){
    Node* temp = new Node(d);
    if(head == NULL){
        head = temp;
        tail = temp;
        return;
    }
    temp->next = head;
    head = temp;
}

void print(Node* head){
    Node* curr = head;
    if(curr == NULL){
        cout << "No element found" << endl;
        return;
    }
    while(curr != NULL){
        cout << curr->data << "  ";
        curr = curr->next;
    }
    cout << endl;
}

void insertAtTail(Node* &head, Node* &tail, int d){
    Node* temp = new Node(d);
    if(tail == NULL){ // means head will also be NULL
        head = temp;
        tail = temp;
        return;
    }
    tail->next = temp;
    tail = temp;
}

Node* reverseLinkedList(Node *head){
    if(head == NULL || head->next == NULL){
        return head;
    }

    Node* currNode = head;
    Node* prevNode = NULL;
    while(currNode != NULL){
        Node* nextNode = currNode->next;
        currNode->next = prevNode;
        prevNode = currNode;
        currNode = nextNode;
    }
    return prevNode;
}
// Recursive way to reverse a LinkedList
Node* reverse2(Node* &head, Node* &prevNode, Node* &nextNode){
    // base case 
    if(head == NULL || head->next == NULL){
        return head;
    }
    // recursive relation

    reverse2(head, head, head->next);
}

Node* reverseLinkedList2(Node *head){
    Node* prevNode = NULL;
    Node* nextNode = NULL;
    reverse2(head, prevNode, nextNode);
}

int main()
{
    Node* head = NULL;
    Node* tail = NULL;
    insertAtHead(head, tail, 12);
    insertAtHead(head, tail, 20);
    insertAtHead(head, tail, 30);
    insertAtTail(head, tail, 40);
    insertAtTail(head, tail, 50);
    print(head);
    head = reverseLinkedList(head);
    print(head);
    return 0;
}

