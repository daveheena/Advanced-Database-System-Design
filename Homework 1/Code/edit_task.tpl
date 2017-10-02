<form action="/edittask" method="POST">
    <table border=1 style="border-collapse:collapse;border-spacing:10px">    
        <tr>
            <td>Task Name:</td>
            <td><select name="task_name">
                %for row in rows:
                    <option value="{{row[0]}}">{{row[1]}}</option>
                %end
            </select></td>
        </tr>
        <tr>
            <td>Updated Task Name:</td>
            <td><input type="text" name="new_task_name"/></td>
        </tr>
        <tr>
            <td>Task Status:</td>
            <td><select name="task_status">
                <option value="New">New</option>
                <option value="Pending">Pending</option>
                <option value="In Progress">In Progress</option>
                <option value="Completed">Completed</option>
            </select></td>
        </tr>
        <tr>
            <td>Task Priority:</td>
            <td><select name="task_priority">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select></td>
        </tr>
        <tr>
            <td colspan="2"><input type="submit" value="Update Task"/></td>
        </tr>
    </table>
</form>