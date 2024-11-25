import cloudinary.uploader
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProfileSerializer, ProfileFollowingSerializer
from .models import ProfileModel, ProfileFollowingModel
from .permissions import IsAuthorOrAdmin
import cloudinary

# Create your views here.


class CurrentUserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]

    def get_object(self):
        current_user = self.request.user
        current_user_profile = self.queryset.get(user=current_user)
        if current_user_profile is not None:
            return current_user_profile


class CurrentUserUpdateProfilePictureAPIView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    parser_classes = [MultiPartParser, JSONParser]

    def get_object(self):
        current_user = self.request.user
        current_user_profile = self.queryset.get(user=current_user)
        if current_user_profile is not None:
            return current_user_profile

    def perform_update(self, serializer):
        file = self.request.data.get('image')
        upload_data = cloudinary.uploader.upload(
            file=file, folder='pollogram/profile')
        image_id: str = upload_data['public_id']
        obj = serializer.instance
        obj.profile_picture = image_id
        serializer.save()


class UserProfileListAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProfileModel.objects.all()
    lookup_field = 'pk'


class UserProfileCreateFollowAPIView(CreateAPIView):
    serializer_class = ProfileFollowingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProfileFollowingModel.objects.all()
    lookup_field = 'pk'

    def perform_create(self, serializer):
        # print(self.request.get('pk'))
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_user_prifile = ProfileModel.objects.get(id=self.kwargs['pk'])
        if target_user_prifile is not None:
            serializer.save(user_profile=current_user_profile,
                            following_user_id=target_user_prifile)
        # obj = serializer.instance
        # obj.following_user_id = '2'
        # serializer.save()
        # return serializer.save(following_user_id=self.kwargs['pk'])
        # self.queryset.create
