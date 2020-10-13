// { Driver Code Starts
    import java.util.*;

    class Node
    {
        int data;
        Node next;
        
        Node(int d)
        {
            data = d;
            next = null;
        }
    }
    
    class Is_LinkedList_Palindrom
    {
         Node head;  
         Node tail;
        
        /* Function to print linked list */
        void printList(Node head)
        {
            Node temp = head;
            while (temp != null)
            {
               System.out.print(temp.data+" ");
               temp = temp.next;
            }  
            System.out.println();
        }
        
     
        /* Inserts a new Node at front of the list. */
        public void addToTheLast(Node node) 
        {
    
            if (head == null) 
            {
                head = node;
                tail = node;
            } else 
            {
                tail.next = node;
                tail = node;
            }
        }
        
        public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
             
            while(t>0)
            {
                int n = sc.nextInt();
                //int k = sc.nextInt();
                Is_LinkedList_Palindrom llist = new Is_LinkedList_Palindrom();
                //int n=Integer.parseInt(br.readLine());
                int a1=sc.nextInt();
                Node head= new Node(a1);
                Node tail = head;
                for (int i = 1; i < n; i++) 
                {
                    int a = sc.nextInt(); 
                    tail.next = new Node(a);
                    tail = tail.next;
                }
                
                Palindrome g = new Palindrome();
                if(g.isPalindrome(head) == true)
                    System.out.println(1);
                else
                    System.out.println(0);
                t--;
            }
            
        }
    }
    
    
    
    // } Driver Code Ends
    
    
    /* Structure of class Node is
    class Node
    {
        int data;
        Node next;
        
        Node(int d)
        {
            data = d;
            next = null;
        }
    }*/
    
    class Palindrome
    {
        // Function to check if linked list is palindrome
        boolean isPalindrome(Node head) 
        {
            //Your code here
            String a = "";
            while (head!=null) {
                a= a+head.data;
                head = head.next;
            }
            String temp = reverse(a);
            if (a.equals(temp)){
                return true;
            }              

                return false;
            
        }     
        String reverse(String str) {
            StringBuilder sb=new StringBuilder(str);  
            sb.reverse();  
            return sb.toString();
        }
    }
    
    