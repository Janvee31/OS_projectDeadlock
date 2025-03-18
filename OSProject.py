# GUI Implementation
class DeadlockToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Prevention and Recovery Toolkit")

        # Input fields
        self.processes_label = tk.Label(root, text="Processes (comma-separated):")
        self.processes_label.grid(row=0, column=0)
        self.processes_entry = tk.Entry(root)
        self.processes_entry.grid(row=0, column=1)

        self.resources_label = tk.Label(root, text="Resources (comma-separated):")
        self.resources_label.grid(row=1, column=0)
        self.resources_entry = tk.Entry(root)
        self.resources_entry.grid(row=1, column=1)

        self.available_label = tk.Label(root, text="Available Resources (comma-separated):")
        self.available_label.grid(row=2, column=0)
        self.available_entry = tk.Entry(root)
        self.available_entry.grid(row=2, column=1)

        self.max_need_label = tk.Label(root, text="Max Need (rows for processes, comma-separated):")
        self.max_need_label.grid(row=3, column=0)
        self.max_need_entry = tk.Entry(root)
        self.max_need_entry.grid(row=3, column=1)

        self.allocation_label = tk.Label(root, text="Allocation (rows for processes, comma-separated):")
        self.allocation_label.grid(row=4, column=0)
        self.allocation_entry = tk.Entry(root)
        self.allocation_entry.grid(row=4, column=1)

        # Buttons
        self.check_safe_button = tk.Button(root, text="Check Safe State", command=self.check_safe_state)
        self.check_safe_button.grid(row=5, column=0)

        self.detect_deadlock_button = tk.Button(root, text="Detect Deadlock", command=self.detect_deadlock)
        self.detect_deadlock_button.grid(row=5, column=1)

        self.draw_graph_button = tk.Button(root, text="Draw Resource Allocation Graph", command=self.draw_graph)
        self.draw_graph_button.grid(row=6, column=0, columnspan=2)

    def check_safe_state(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            available = list(map(int, self.available_entry.get().split(',')))
            max_need = [list(map(int, row.split(','))) for row in self.max_need_entry.get().split(';')]
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]

            banker = BankersAlgorithm(processes, resources, available, max_need, allocation)
            is_safe, safe_sequence = banker.is_safe()

            if is_safe:
                messagebox.showinfo("Safe State", f"The system is in a safe state. Safe sequence: {safe_sequence}")
            else:
                messagebox.showwarning("Unsafe State", "The system is in an unsafe state. Deadlock may occur.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def detect_deadlock(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            available = list(map(int, self.available_entry.get().split(',')))
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]
            request = [list(map(int, row.split(','))) for row in self.max_need_entry.get().split(';')]

            if detect_deadlock(allocation, request, available):
                messagebox.showwarning("Deadlock Detected", "A deadlock has been detected in the system.")
            else:
                messagebox.showinfo("No Deadlock", "No deadlock detected.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def draw_graph(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]
            request = [list(map(int, row.split(','))) for row in self.max_need_entry.get().split(';')]

            draw_resource_allocation_graph(allocation, request, processes, resources)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")