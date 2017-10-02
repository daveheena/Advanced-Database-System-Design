<form action="/deletetask" method="POST">
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
            <td colspan="2"><input type="submit" value="Delete Task"/></td>
        </tr>
    </table>
</form>