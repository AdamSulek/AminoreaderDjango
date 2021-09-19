from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Aminoreader
from rest_framework.decorators import action
from django.http import JsonResponse, HttpResponseRedirect
from django.core.files.storage import default_storage, FileSystemStorage
import requests
from django.shortcuts import render
import re
from .amino_dictionary import AMINO_LETTER, AMINO_DICT

class AminoreaderView(ModelViewSet):
    queryset = Aminoreader.objects.all()
    serializer_class = FileSerializer

    @action(methods=['get'], detail=False)
    def newest_file(self, request):
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        #return Response(serializer.data['file'])
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def upload_file(self, request):
        context = {}
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        file_path = str(serializer.data['file'])
        page = 'http://0.0.0.0:8000' + file_path
        print("page: {}".format(page))
        text = requests.get(page)
        context['text'] = text.content

        return Response(context)

    @action(methods=['get'], detail=False)
    def mass_calc(self, request):
        context = {}
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        file_path = str(serializer.data['file'])
        page = 'http://0.0.0.0:8000' + file_path
        print("page: {}".format(page))
        text = requests.get(page)
        context['text'] = text.content
        t = str(text.content)
        threes = [t[i:i+3] for i in range(2, len(t)-4, 3)]
        mass = 0
        for amino in threes:
            last = AMINO_DICT[amino][-1]
            mass += last
        context['mass'] = mass
        context['threes'] = threes
        return Response(context)

    @action(methods=['get'], detail=False)
    def nuclotide_to_amino(self, request):
        context = {}
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        file_path = str(serializer.data['file'])
        page = 'http://0.0.0.0:8000' + file_path
        print("page: {}".format(page))
        text = requests.get(page)
        dirty_text = str(text.content)
        sequence = ''
        for line in dirty_text.split():
            pack = re.findall(r'[ACGT]{3,}', line)
            if pack:
                sequence += str(pack[0])
        context['sequence'] = sequence

        threes = [sequence[i:i+3] for i in range(0, len(sequence)-1, 3)]
        amino_sequence = ''
        for codon in threes:
            for key, val in AMINO_DICT.items():
                if codon in val:
                    amino_sequence += key

        context['aminoacids'] = amino_sequence
        return Response(context)


    @action(methods=['get'], detail=False)
    def one_to_three(self, request):
        context = {}
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        file_path = str(serializer.data['file'])
        page = 'http://0.0.0.0:8000' + file_path
        print("page: {}".format(page))
        text = requests.get(page)
        seq = str(text.content)
        amino_seq = ''
        for amino in seq:
            for k, v in AMINO_LETTER.items():
                if amino == v:
                    amino_seq += k
        context['seq'] = amino_seq

        return Response(context)
