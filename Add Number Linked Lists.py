class Solution:
    def addTwoLists(self, num1, num2):
        # Helper function to reverse a linked list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        # Step 1: Reverse both lists taaki addition easier ho (unit place se start kar sake)
        num1 = reverse(num1)
        num2 = reverse(num2)

        carry = 0
        dummy = Node(0)
        tail = dummy

        # Step 2: Dono list mein jab tak digits hai ya carry bacha hai
        while num1 or num2 or carry:
            val1 = num1.data if num1 else 0
            val2 = num2.data if num2 else 0

            total = val1 + val2 + carry
            carry = total // 10  # Carry nikal lo
            digit = total % 10   # Current digit store karo

            # Naya node banao aur jod do
            tail.next = Node(digit)
            tail = tail.next

            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

        # Step 3: Final answer ko reverse kar do (kyunki humne pehle reverse kiya tha)
        result = reverse(dummy.next)

        # Step 4: Leading 0s ko hata do agar ho (edge case handle)
        while result and result.data == 0 and result.next:
            result = result.next

        return result
