<table border=1 style="border-collapse:collapse;border-spacing:10px;">
%for index,row in enumerate(rows):
    %if(index==0):
        <tr>
            <th>Task ID</th>
            <th>Task Name</th>
            <th>Task Status</th>
            <th>Task Priority</th>
        </tr>
    %end
    <tr>        
        %for col in row:
            <td>{{col}}</td>               
        %end
    </tr>
%end
</table>