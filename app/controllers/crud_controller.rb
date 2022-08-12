# -*- encoding : utf-8 -*-
class CrudController < ApplicationController
  def index
    collection

    if params[:filter] && params[:filter][:term].present?
      @term = params[:filter][:term]

      @resources = @resources.basic_search(@term)
    end
  end

  def new
    @resource = @klass.new
    session[:back_to] = params[:back_to]
  end

  def edit
    @resource = @klass.find(params[:id])
  end

  def show
    @resource = @klass.find(params[:id])
  end

  def create
    @resource = @klass.new(resource_params)
    if @resource.save
      flash[:notice] = 'Salvo'
      if session[:back_to]
        redirect_to String.new(session[:back_to])
        session[:back_to] = nil
      elsif params[:commit] != 'Salvar'
        redirect_to send("#{@klass.model_name.param_key.pluralize}_path")
      else
        redirect_to send("edit_#{@klass.model_name.param_key}_path", @resource)
      end
    else
      flash[:error] = @resource.errors.full_messages.join('. ')
      render :action => 'new'
    end
  end

  def update
    @resource = @klass.find(params[:id])
    if @resource.update_attributes(resource_params)
      flash[:notice] = 'Atualizado'
      if params[:commit] == 'Salvar'
        redirect_to send("edit_#{@klass.model_name.param_key}_path", @resource)
      else
        redirect_to send("#{@klass.model_name.param_key.pluralize}_path")
      end
    else
      flash[:error] = @resource.errors.full_messages.join('. ')
      render :action => 'edit'
    end
  end

  def destroy
    @resource = @klass.find(params[:id])
    @resource.destroy
    redirect_to send("#{@klass.model_name.param_key.pluralize}_path")
  end

  protected

  def set_klass(klass)
    @klass = klass
  end

  def set_search_attrs(attrs)
    @search_attrs = attrs
  end

  def readonly
    @readonly = true
  end

  private

  def collection
    @resources ||= @klass.paginate(page: params[:page], per_page: 30).order('created_at desc')
  end

  def save_resource_in_session
    session[@resource.class.to_s.downcase] = @resource.id if @resource
  end
end
