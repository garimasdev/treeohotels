import traceback
from urllib import request
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from hotels.models import *



# customer dashboard
@login_required
def customer_dashboard(request):
    return render(request, 'db-dashboard.html')



# vendor or agent dashboard 
@login_required
def vendor_dashboard(request):
    return render(request, 'db-vendor-dashboard.html')




"""
VENDOR HOTEL DASHBOARD SERVICE
"""

@login_required
def vendor_hotel(request):
    return render(request, 'db-vendor-add-hotel.html')


@login_required
def add_hotel(request):
    if request.method == 'POST':
        try:
            # Step 1: Retrieve the data from the request
            hotel_name = request.POST.get("hotel_name")
            description = request.POST.get("description")
            youtube_video = request.POST.get("youtube_video")
            hotel_rating = request.POST.get("hotel_rating")

            # Handle image uploads
            banner_image = request.FILES.get("banner_image")
            featured_image = request.FILES.get("featured_image")
            gallery_images = request.FILES.getlist("gallery_images")


            # Step 4: Create the Hotel object manually
            hotel = Hotel.objects.create(
                name=hotel_name,
                description=description,
                youtube_video=youtube_video,
                hotel_rating=hotel_rating,
                vendor=request.user
            )

            request.session['hotel_id'] = hotel.id

            # Step 5: Handle the images
            if banner_image:
                HotelImage.objects.create(hotel=hotel, image=banner_image, image_type="banner")
            if featured_image:
                HotelImage.objects.create(hotel=hotel, image=featured_image, image_type="featured")
            for image in gallery_images:
                HotelImage.objects.create(hotel=hotel, image=image, image_type="gallery")
            
            # Step 6: Handle the hotel policies
            policy_titles = [request.POST.get(f"policy_title_{i}") for i in range(1, len(request.POST) + 1)]
            policy_contents = [request.POST.get(f"policy_content_{i}") for i in range(1, len(request.POST) + 1)]
        
            for title, content in zip(policy_titles, policy_contents):
                if title and content:
                    HotelPolicy.objects.create(hotel=hotel, title=title, content=content)

            # Step 7: Return a response
            return JsonResponse({"message": "Hotel created successfully!"}, status=201)
        except:
            traceback.print_exc()

    return render(request, "db-vendor-add-hotel.html")



@login_required
def add_hotel_location(required):
    if request.method == 'POST':
        pass



@login_required
def add_hotel_pricing(request):
    if request.method == 'POST':
        try:
            hotel_id = request.session.get('hotel_id')
            try:
                hotel = Hotel.objects.get(id=hotel_id)
            except Hotel.DoesNotExist:
                return JsonResponse({'error': 'Hotel not found'}, status=404)

            hotel_price = request.POST.get('hotel_price')
            check_in_time = request.POST.get('check_in_time')
            check_out_time = request.POST.get('check_out_time')
            min_advance_reservations = request.POST.get('min_advance_reservations')
            min_day_stay_requirements = request.POST.get('min_day_stay_requirements')

            # Update existing or create a new pricing entry
            pricing, created = HotelPricing.objects.update_or_create(
                hotel=hotel,
                defaults={
                    'price': hotel_price,
                    'check_in_time': check_in_time,
                    'check_out_time': check_out_time,
                    'minimum_advance_reservations': min_advance_reservations,
                    'minimum_day_stay_requirements': min_day_stay_requirements
                }
            )

            return JsonResponse({'message': 'Hotel pricing details saved successfully', 'created': created})

        except:
            traceback.print_exc()
    else:
        return render(request, "db-vendor-add-hotel.html")




@login_required
def update_hotel_services(request):
    # Retrieve hotel ID from session
    hotel_id = request.session.get('hotel_id')

    if hotel_id:
        try:
            # Retrieve or create HotelServices object
            hotel_services, created = HotelServices.objects.get_or_create(hotel_id=hotel_id)

            # Update the fields based on the form submission
            hotel_services.apartment = 'apartment' in request.POST
            hotel_services.boat = 'boat' in request.POST
            hotel_services.holiday_home = 'holiday_home' in request.POST
            hotel_services.villa = 'villa' in request.POST
            hotel_services.cabin = 'cabin' in request.POST
            hotel_services.hostel = 'hostel' in request.POST
            hotel_services.lodge = 'lodge' in request.POST
            hotel_services.mansion = 'mansion' in request.POST
            hotel_services.banquet = 'banquet' in request.POST

            # Facilities
            hotel_services.swimming_pool = 'swimming_pool' in request.POST
            hotel_services.gym = 'gym' in request.POST
            hotel_services.spa = 'spa' in request.POST
            hotel_services.parking = 'parking' in request.POST
            hotel_services.restaurant = 'restaurant' in request.POST
            hotel_services.bar = 'bar' in request.POST
            hotel_services.free_wifi = 'free_wifi' in request.POST
            hotel_services.conference_room = 'conference_room' in request.POST

            # Hotel Services
            hotel_services.room_service = 'room_service' in request.POST
            hotel_services.cleaning_service = 'cleaning_service' in request.POST
            hotel_services.laundry_service = 'laundry_service' in request.POST
            hotel_services.shuttle_service = 'shuttle_service' in request.POST
            hotel_services.concierge_service = 'concierge_service' in request.POST
            hotel_services.hour24_reception = 'hour24_reception' in request.POST

            # Save the updated services
            hotel_services.save()

            if created:
                return JsonResponse({'message': 'Hotel services created successfully!'})
            else:
                return JsonResponse({'message': 'Hotel services updated successfully!'})
        except:
            traceback.print_exc()
    else:
        return render(request, "db-vendor-add-hotel.html")





"""
VENDOR ROOM DASHBOARD SERVICE
"""
@login_required
def vendor_room(request):
    return render(request, 'db-vendor-add-room.html')