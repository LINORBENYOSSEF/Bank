
function flightHtml(flight) {
    return `
    <div class="card bg-secondary">
        <div name="flight-root" class="card-body" data-flight-id="${flight.id}"
            onclick="viewFlight('${flight.id}')">
            <h6 class="side-by-side-header">
                ${flight.departure.city}, ${flight.departure.country} ->
                ${flight.destination.city}, ${flight.destination.country}
            </h6>
            <div>${flight.airline.name}</div>
            <div>${flight.ticket_cost} $</div>
        </div>
    </div>
    `;
}

function loadFlights(offset,
                    limit,
                    reload = false,
                    callback = null) {
    $.ajax({
        method: "GET",
        url: "/api/flight/",
        contentType: "application/json",
        data: {
            limit: limit,
            offset: offset
        }
    }).done(function(data) {
        if (reload) {
            $('#flights-container').empty();
        }
        $.each(data, function(i, item) {
            $('#flights-container').append(flightHtml(item));
        });

        if (callback != null) {
            callback(data.length);
        }
    });
}


function viewFlight(flightId) {
    $.ajax({
        method: "GET",
        url: `/api/flight/${flightId}`,
        contentType: "application/json"
    }).done(function(data) {
        console.log(data);
        var modal = $('#view-flight-modal');

        modal.find('.modal-title').html(flightId);
        modal.find('input[name="time-field"]').val(`${new Date(data.departure_time).toLocaleString()}`);
        modal.find('input[name="departure-field"]').val(`${data.departure.city}, ${data.departure.country}`);
        modal.find('input[name="destination-field"]').val(`${data.destination.city}, ${data.destination.country}`);
        modal.find('input[name="price-field"]').val(`${data.ticket_cost} Dollars`);
        modal.modal('toggle');
    });
}
