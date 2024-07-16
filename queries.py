import sqlite3
from flask import request, jsonify

from utils import validate_cpf

def find_by_cpf():
    try:
        conn = sqlite3.connect('basecpf.db')
        cursor = conn.cursor()

        cpf = request.args.get('cpf')
        if not cpf:
            return jsonify({"error": "CPF is required"}), 400

        if not validate_cpf(cpf):
            return jsonify({"error": "Invalid CPF format"}), 400

        cursor.execute("SELECT * FROM cpf WHERE cpf = ?", (cpf,))
        result = cursor.fetchall()

        if not result:
            return jsonify({"error": "CPF not found"}), 404

        columns = [desc[0] for desc in cursor.description]
        result_dict = [dict(zip(columns, row)) for row in result]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            conn.close()

def find_by_name():
    try:
        conn = sqlite3.connect('basecpf.db')
        cursor = conn.cursor()

        name = request.args.get('name')
        if not name:
            return jsonify({"error": "Name is required"}), 400

        if len(name) < 3:
            return jsonify({"error": "Invalid name"}), 400
        
        name = name.upper()

        cursor.execute("SELECT * FROM cpf WHERE nome = ?", (name,))
        result = cursor.fetchall()

        if not result:
            return jsonify({"error": "Name not found"}), 404

        columns = [desc[0] for desc in cursor.description]
        result_dict = [dict(zip(columns, row)) for row in result]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            conn.close()

def find_by_similar_name():
    try:
        conn = sqlite3.connect('basecpf.db')
        cursor = conn.cursor()

        name = request.args.get('name')
        if not name:
            return jsonify({"error": "Name is required"}), 400

        if len(name) < 3:
            return jsonify({"error": "Invalid name"}), 400
        
        name = f'%{name.upper()}%'

        cursor.execute("SELECT * FROM cpf WHERE nome LIKE ?", (name,))
        result = cursor.fetchall()

        if not result:
            return jsonify({"error": "Name not found"}), 404

        columns = [desc[0] for desc in cursor.description]
        result_dict = [dict(zip(columns, row)) for row in result]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            conn.close()

def find_by_razao():
    try:
        conn = sqlite3.connect('basecnpj.db')
        cursor = conn.cursor()

        name = request.args.get('razao')
        if not name:
            return jsonify({"error": "Razao Social is required"}), 400

        if len(name) < 3:
            return jsonify({"error": "Invalid razao social"}), 400
        
        name = name.upper()

        cursor.execute("SELECT * FROM empresas WHERE razao = ?", (name,))
        result = cursor.fetchall()

        if not result:
            return jsonify({"error": "Razao not found"}), 404

        columns = [desc[0] for desc in cursor.description]
        result_dict = [dict(zip(columns, row)) for row in result]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            conn.close()

def find_by_similar_razao():
    try:
        conn = sqlite3.connect('basecnpj.db')
        cursor = conn.cursor()

        name = request.args.get('razao')
        if not name:
            return jsonify({"error": "Razao is required"}), 400

        if len(name) < 3:
            return jsonify({"error": "Invalid razao"}), 400
        
        name = f'%{name.upper()}%'

        cursor.execute("SELECT * FROM empresas WHERE razao LIKE ?", (name,))
        result = cursor.fetchall()

        if not result:
            return jsonify({"error": "Razao not found"}), 404

        columns = [desc[0] for desc in cursor.description]
        result_dict = [dict(zip(columns, row)) for row in result]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn:
            conn.close()

def find_by_name_cpf():
    try:
        conn_cpf = sqlite3.connect('basecpf.db')
        conn_cnpj = sqlite3.connect('basecnpj.db')
        cursor_cpf = conn_cpf.cursor()
        cursor_cnpj = conn_cnpj.cursor()

        name = request.args.get('name')
        cpf = request.args.get('cpf')

        if not name and not cpf:
            return jsonify({"error": "Name or CPF is required"}), 400

        if cpf and not validate_cpf(cpf):
            return jsonify({"error": "Invalid CPF format"}), 400

        results = []

        if name:
            name = f'%{name.upper()}%'
            cursor_cnpj.execute("SELECT * FROM empresas WHERE razao LIKE ?", (name,))
            results.extend(cursor_cnpj.fetchall())

        if cpf:
            cursor_cpf.execute("SELECT * FROM cpf WHERE cpf = ?", (cpf,))
            cpf_results = cursor_cpf.fetchall()
            if cpf_results:
                for row in cpf_results:
                    name_from_cpf = row[1].upper()  
                    cursor_cnpj.execute("SELECT * FROM empresas WHERE razao LIKE ?", (f'%{name_from_cpf}%',))
                    results.extend(cursor_cnpj.fetchall())

        if not results:
            return jsonify({"error": "No results found"}), 404

        columns_cnpj = [desc[0] for desc in cursor_cnpj.description]
        result_dict = [dict(zip(columns_cnpj, row)) for row in results]

        return jsonify(result_dict), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conn_cpf:
            conn_cpf.close()
        if conn_cnpj:
            conn_cnpj.close()