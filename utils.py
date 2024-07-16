def validate_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()