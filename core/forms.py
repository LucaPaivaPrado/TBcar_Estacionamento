from django.forms import ModelForm
from core.models import Cliente,Veiculo,Marca,Tabela,Mensalista,Rotativo
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class FormCliente(ModelForm):


    class Meta:
        model = Cliente
        fields = '__all__'      #ou [] e digita o que voce quiser expecificamente

class FormVeiculo(ModelForm):


    class Meta:
        model = Veiculo
        fields = '__all__'

class FormMarca(ModelForm):


    class Meta:
        model = Marca
        fields = '__all__'

class FormTabela(ModelForm):


    class Meta:
        model = Tabela
        fields = '__all__'

class FormMensalista(ModelForm):


    class Meta:
        model = Mensalista
        fields = '__all__'

class FormRotativo(ModelForm):


    class Meta:
        model = Rotativo
        fields = '__all__'
        widgets = {'entrada':DateTimePickerInput(),'saida':DateTimePickerInput()}

