$(function() {
    $('#add_item').click(function() {
        const newItem = $('<li>item</li>')
        $('UL.my_list').append(newItem)
    })
})
